from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e06e7ddc-ec19-5d51-a610-26ea2593da95",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaDelphoxex.Name",
    display_name="Mega Delphox ex",
    searchable_by=["Mega Delphox ex", "Stage 2", "MEGA", "ex", "MegaDelphoxex"],
    subtypes=["Stage 2", "MEGA", "ex"],
    collector_number=8,
    set_code="ME5",
    rarity=Rarities.Rare,
    hp=350,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Braixen.Name",
    family_id=655,
    abilities=[
        Attack(
            title="Trick Portal",
            game_text="Look at the top 9 cards of your deck, and you may put any number of Pok\u00e9mon you find there onto your Bench. Shuffle the other cards back into your deck.",
            cost={PokemonTypes.FIRE: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Eerie Glow",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned and Confused.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=200,
            effect=unimplemented,
        ),
    ],
)