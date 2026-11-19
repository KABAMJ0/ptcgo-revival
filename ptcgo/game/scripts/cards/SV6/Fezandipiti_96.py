from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import count_energy, damage_per

card = PokemonCardDef(
    guid="35ca3583-e883-599d-83d8-da88c1096284",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Fezandipiti.Name",
    display_name="Fezandipiti",
    searchable_by=["Fezandipiti", "Basic", "Fezandipiti"],
    subtypes=["Basic"],
    collector_number=96,
    set_code="SV6",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    abilities=[
        Ability(
            title="Adrena-Pheromone",
            game_text="If this Pok\u00e9mon has any Darkness Energy attached and is damaged by an attack, flip a coin. If heads, prevent that damage.",
            effect=unimplemented,
        ),
        Attack(
            title="Energy Feather",
            game_text="This attack does 30 damage for each Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            damage_operator="x",
            effect=damage_per(count_energy("self"), 30),
        ),
    ],
)