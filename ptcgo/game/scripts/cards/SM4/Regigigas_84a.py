from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import discard_stadium_attack
from ptcgo.game.card_effects.passives_common import pokemon_named
from ptcgo.game.session.passives import Passive, carrier_pokemon


def _bench_area(pokemon):
    """The owner's Bench area, reached through the entity tree (a passive's
    blocks_attack hook is not handed the board)."""
    player = getattr(getattr(pokemon, "parent", None), "parent", None)
    for area in getattr(player, "children", None) or []:
        if area.get_attribute(AttrID.NAME) == "bench":
            return area
    return None


class SealOfAntiquityPassive(Passive):
    """Can't attack unless Regirock, Regice and Registeel are on your Bench."""

    NAMES = ("Regirock", "Regice", "Registeel")

    def blocks_attack(self, pokemon, carrier):
        if pokemon is not carrier_pokemon(carrier):
            return False
        bench = _bench_area(pokemon)
        benched = list(getattr(bench, "children", None) or [])
        return not all(
            any(pokemon_named(name)(other) for other in benched)
            for name in self.NAMES
        )


card = PokemonCardDef(
    guid="96df9775-c78d-56c7-82a7-b7c88af5a3a5",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Regigigas.Name",
    display_name="Regigigas",
    searchable_by=["Regigigas", "Basic", "Regigigas"],
    subtypes=["Basic"],
    collector_number=84,
    set_code="SM4",
    rarity=Rarities.RareHolo,
    hp=180,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=486,
    abilities=[
        Ability(
            title="Seal of Antiquity",
            game_text="This Pok\u00e9mon can't attack unless Regirock, Regice, and Registeel are on your Bench.",
            passive=SealOfAntiquityPassive(),
        ),
        Attack(
            title="Giant Stomp",
            game_text="Discard any Stadium card in play.",
            cost={PokemonTypes.COLORLESS: 5},
            damage=160,
            effect=discard_stadium_attack(),
        ),
    ],
)