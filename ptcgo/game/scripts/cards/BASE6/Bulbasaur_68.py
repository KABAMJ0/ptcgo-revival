from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7fd2c813-bf24-5e86-afa8-b73a2230744e",
    key="BASE6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bulbasaur.Name",
    display_name="Bulbasaur",
    searchable_by=["Bulbasaur", "Basic", "Bulbasaur"],
    subtypes=["Basic"],
    collector_number=68,
    set_code="BASE6",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=1,
    abilities=[
        Attack(
            title="Leech Seed",
            game_text="Unless all damage from this attack is prevented, you may remove 1 damage counter from Bulbasaur.",
            cost={PokemonTypes.GRASS: 2},
            damage=20,
            effect=unimplemented,
        ),
    ],
)