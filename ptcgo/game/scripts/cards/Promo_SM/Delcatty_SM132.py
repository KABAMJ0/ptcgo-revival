from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.attacks_common import on_evolve
from ptcgo.game.data_utils import Triggers
from ptcgo.game.attributes import AttrID

async def search_for_friends(ctx):
    """On evolve: put up to 2 Supporter cards from the deck into the hand."""
    from ptcgo.game.attributes import TrainerType
    await search_to_hand(
        lambda c: c.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.SUPPORTER.value,
        2, prompt="Choose up to 2 Supporter cards")(ctx)


card = PokemonCardDef(
    guid="488ecf73-f09a-57d4-ae67-9ec066125778",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Delcatty.Name",
    display_name="Delcatty",
    searchable_by=["Delcatty", "Stage 1", "Delcatty"],
    subtypes=["Stage 1"],
    collector_number=132,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Skitty.Name",
    family_id=301,
    abilities=[
        Ability(
            title="Search for Friends",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may put 2 Supporter cards from your discard pile into your hand.",
            trigger=Triggers.ON_EVOLVE,
            effect=on_evolve(search_for_friends),
        ),
        Attack(
            title="Cat Kick",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)