from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2e7def90-2108-51e1-ac4c-9fb8218e1dd4",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Regirock.Name",
    display_name="Regirock",
    searchable_by=["Regirock", "Basic", "Regirock"],
    subtypes=["Basic"],
    collector_number=82,
    set_code="SV9",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=377,
    abilities=[
        Ability(
            title="Rock Armor",
            game_text="If this Pok\u00e9mon has any Energy attached, it takes 30 less damage from attacks (after applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Breaching Lariat",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 3},
            damage=120,
            effect=unimplemented,
        ),
    ],
)