from ptcgo.game.data_utils import PokemonCardDef, Attack
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import count_energy, damage_per
from ptcgo.game.card_effects.support_common import switch_self_attack


card = PokemonCardDef(
    guid="0ff8e615-0321-58d4-9b41-549f6960143c",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Laprasex.Name",
    display_name="Lapras ex",
    searchable_by=["Lapras ex", "Basic", "ex", "Laprasex"],
    subtypes=["Basic", "ex"],
    collector_number=22,
    set_code="ME3",
    rarity=Rarities.Rare,
    hp=210,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=131,
    abilities=[
        Attack(
            title="Hydro Turn",
            game_text="This attack does 30 damage for each Water Energy attached to this Pok\u00e9mon. Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            damage_operator="x",
            effect=damage_per(count_energy("self", PokemonTypes.WATER), 30,
                              also=switch_self_attack(damage=0)),
        ),
        Attack(
            title="Surf",
            cost={PokemonTypes.WATER: 3},
            damage=140,
        ),
    ],
)