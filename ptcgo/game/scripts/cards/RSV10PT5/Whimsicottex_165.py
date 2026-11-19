from ptcgo.game.card_effects.trainers import is_basic_energy_card
from ptcgo.game.card_effects.support_common import search_attach_energy
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.session.effects import is_trainer_card


async def poltergeist(ctx):
    """Opponent reveals their hand; 50 damage for each Trainer card found there."""
    cards = await ctx.reveal_hand(of_player=ctx.opponent_id)
    count = sum(1 for c in cards if is_trainer_card(c))
    await ctx.deal_damage(50 * count)


card = PokemonCardDef(
    guid="27a051b5-db7b-58fd-94f0-c1881da5772d",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Whimsicottex.Name",
    display_name="Whimsicott ex",
    searchable_by=["Whimsicott ex", "Stage 1", "ex", "Whimsicottex"],
    subtypes=["Stage 1", "ex"],
    collector_number=165,
    set_code="RSV10PT5",
    rarity=Rarities.Rare,
    hp=230,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cottonee.Name",
    family_id=546,
    abilities=[
        Attack(
            title="Energy Gift",
            game_text="Search your deck for up to 3 Basic Energy cards and attach them to your Pok\u00e9mon in any way you like. Then, shuffle your deck.",
            cost={PokemonTypes.GRASS: 1},
            effect=search_attach_energy(predicate=is_basic_energy_card, count=3, to_self=True),
        ),
        Attack(
            title="Wondrous Cotton",
            game_text="Your opponent reveals their hand. This attack does 50 damage for each Trainer card you find there.",
            cost={PokemonTypes.GRASS: 1},
            damage=50,
            damage_operator="x",
            effect=poltergeist,
        ),
    ],
)