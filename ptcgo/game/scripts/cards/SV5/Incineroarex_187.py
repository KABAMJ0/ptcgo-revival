from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="258023c0-1910-57e5-8c02-edbe0e21e707",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Incineroarex.Name",
    display_name="Incineroar ex",
    searchable_by=["Incineroar ex", "Stage 2", "ex", "Incineroarex"],
    subtypes=["Stage 2", "ex"],
    collector_number=187,
    set_code="SV5",
    rarity=Rarities.Rare,
    hp=320,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Torracat.Name",
    family_id=725,
    abilities=[
        Ability(
            title="Hustle Play",
            game_text="Attacks used by this Pok\u00e9mon cost Colorless less for each of your opponent's Benched Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Blaze Blast",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 4},
            damage=240,
            effect=unimplemented,
        ),
    ],
)