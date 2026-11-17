from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6387e5a2-6488-5c44-996c-cf421dc06d31",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grapploct.Name",
    display_name="Grapploct",
    searchable_by=["Grapploct", "Stage 1", "Grapploct"],
    subtypes=["Stage 1"],
    collector_number=52,
    set_code="SV4PT5",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Clobbopus.Name",
    family_id=852,
    abilities=[
        Attack(
            title="Slow-Acting Syncope",
            game_text="At the end of your opponent's next turn, the Defending Pok\u00e9mon will be Knocked Out.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Mach Cross",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
    ],
)