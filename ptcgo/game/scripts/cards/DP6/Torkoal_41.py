from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.passives_common import is_in_active_spot
from ptcgo.game.session.passives import Passive


def _my_benched(target, carrier) -> bool:
    parent = getattr(target, "parent", None)
    return (parent is not None
            and parent.get_attribute(AttrID.NAME) == "bench"
            and target.owning_player_id == carrier.owning_player_id
            and is_in_active_spot(carrier))


class _WhiteSmoke(Passive):
    """Torkoal is Active: your Benched Pokemon take no attack damage or effects."""

    def prevents_damage(self, calc, carrier):
        return bool(calc.is_attack and calc.is_opposing
                    and _my_benched(calc.target, carrier))

    def blocks_attack_effects(self, target, carrier, attacker=None, board=None):
        return _my_benched(target, carrier)

card = PokemonCardDef(
    guid="69a72791-aa18-5a69-a863-b141d3dd539d",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Torkoal.Name",
    display_name="Torkoal",
    searchable_by=["Torkoal", "Basic", "Torkoal"],
    subtypes=["Basic"],
    collector_number=41,
    set_code="DP6",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=324,
    abilities=[
        Ability(
            title="White Smoke",
            game_text="As long as Torkoal is your Active Pok\u00e9mon, prevent all effects, including damage, done to your Benched Pok\u00e9mon by your opponent's attacks.",
            passive=_WhiteSmoke(),
        ),
        Attack(
            title="Black Soot",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Burned and Paralyzed.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.BURNED,
                                    SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)