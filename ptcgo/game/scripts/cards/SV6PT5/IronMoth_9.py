from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, subtypes_for
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import protect_next_turn


def _attacker_has_subtype(*names):
    def pred(attacker):
        return attacker is not None and any(
            name in (subtypes_for(attacker.archetype_id) or [])
            for name in names)
    return pred
from ptcgo.game.card_effects.attacks_common import heal_dealt_attack


card = PokemonCardDef(
    guid="4513cdbb-3905-5083-b86c-62d5da2e411e",
    key="SV6PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronMoth.Name",
    display_name="Iron Moth",
    searchable_by=["Iron Moth", "Basic", "Future", "IronMoth"],
    subtypes=["Basic", "Future"],
    collector_number=9,
    set_code="SV6PT5",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    abilities=[
        Attack(
            title="Suction",
            game_text="Heal from this Pok\u00e9mon the same amount of damage you did to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=heal_dealt_attack(),
        ),
        Attack(
            title="Anachronism Repulsor",
            game_text="During your opponent's next turn, prevent all damage done to this Pok\u00e9mon by attacks from Ancient Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=protect_next_turn(prevent=True, attacker_pred=_attacker_has_subtype("Ancient")),
        ),
    ],
)