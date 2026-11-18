from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="043722e4-4ab2-52d5-90dc-7e0840a82b1f",
    key="COL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Riolu.Name",
    display_name="Riolu",
    searchable_by=["Riolu", "Basic", "Riolu"],
    subtypes=["Basic"],
    collector_number=50,
    set_code="COL",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=447,
    abilities=[
        Attack(
            title="Tumble Over",
            game_text="Riolu can't attack during your next turn.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            effect=unimplemented,
        ),
    ],
)