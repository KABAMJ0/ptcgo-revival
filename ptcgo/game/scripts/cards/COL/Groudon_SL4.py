from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7ede7947-92da-5b4b-9598-866b6127c0a5",
    key="COL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Groudon.Name",
    display_name="Groudon",
    searchable_by=["Groudon", "Basic", "Groudon"],
    subtypes=["Basic"],
    collector_number=4,
    set_code="COL",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    family_id=383,
    abilities=[
        Attack(
            title="Volcano Stomp",
            game_text="Flip a coin. If heads, discard the top 4 cards of your opponent's deck. If tails, discard the top 4 cards of your deck.",
            cost={PokemonTypes.FIGHTING: 4},
            damage=80,
            effect=unimplemented,
        ),
    ],
)