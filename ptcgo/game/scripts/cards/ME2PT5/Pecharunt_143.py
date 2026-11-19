from ptcgo.game.card_effects.passives_common import boost_own_next_turn
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.data_utils import Triggers


async def _gold_coffin(ctx):
    """Knocked Out by attack damage: search the deck for a card into hand."""
    if not ctx.ko_from_attack:
        return
    picks = await ctx.search_deck(
        None, count=1, minimum=0,
        prompt="Choose a card to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="b275d387-d70d-5e18-a6b5-c47583b02686",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pecharunt.Name",
    display_name="Pecharunt",
    searchable_by=["Pecharunt", "Basic", "Pecharunt"],
    subtypes=["Basic"],
    collector_number=143,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=1025,
    abilities=[
        Ability(
            title="Final Chain",
            game_text="If this Pok\u00e9mon is Knocked Out by damage from an attack from your opponent's Pok\u00e9mon, search your deck for a card and put it into your hand. Then, shuffle your deck.",
            trigger=Triggers.ON_KNOCKED_OUT,
            effect=_gold_coffin,
        ),
        Attack(
            title="Mochi Rush",
            game_text="During your next turn, this Pok\u00e9mon's Mochi Rush attack does 50 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
            effect=boost_own_next_turn(50, attack_title="Mochi Rush"),
        ),
    ],
)