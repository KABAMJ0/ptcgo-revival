from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="367ade0d-ef5c-5b1c-a524-ff7f03897fc0",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tatsugiri.Name",
    display_name="Tatsugiri",
    searchable_by=["Tatsugiri", "Basic", "Tatsugiri"],
    subtypes=["Basic"],
    collector_number=186,
    set_code="SV6",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=978,
    abilities=[
        Ability(
            title="Attract Customers",
            game_text="Once during your turn, if this Pok\u00e9mon is in the Active Spot, you may look at the top 6 cards of your deck, reveal a Supporter card you find there, and put it into your hand. Shuffle the other cards back into your deck.",
            effect=unimplemented,
        ),
        Attack(
            title="Surf",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1},
            damage=50,
        ),
    ],
)