from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented
from ptcgo.game.session.effects import is_supporter_card
from ptcgo.game.card_effects.pokemon import in_active_spot
from ptcgo.game.card_effects.support_common import look_at_top
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7734b387-0c3b-5843-a990-437c522b0b09",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tatsugiri.Name",
    display_name="Tatsugiri",
    searchable_by=["Tatsugiri", "Basic", "Tatsugiri"],
    subtypes=["Basic"],
    collector_number=118,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=978,
    abilities=[
        Ability(
            title="Attract Customers",
            game_text="Once during your turn, if this Pok\u00e9mon is in the Active Spot, you may look at the top 6 cards of your deck, reveal a Supporter card you find there, and put it into your hand. Shuffle the other cards back into your deck.",
            activation=Activations.ONCE_PER_TURN,
            condition=in_active_spot,
            effect=look_at_top(6, take=1, predicate=is_supporter_card, rest="shuffle"),
        ),
        Attack(
            title="Surf",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1},
            damage=50,
        ),
    ],
)