from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Triggers
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import heal_attack, cure_conditions_effect


async def _queenly_majesty(ctx):
    revealed = await ctx.reveal_hand(ctx.opponent_id)
    if not revealed:
        return
    await ctx.discard_from_hand(
        1, minimum=1, player_id=ctx.opponent_id,
        prompt="Choose a card from their hand to discard")


card = PokemonCardDef(
    guid="fb3dea45-2a49-5a9f-b3b2-94303853429d",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tsareena.Name",
    display_name="Tsareena",
    searchable_by=["Tsareena", "Stage 2", "Tsareena"],
    subtypes=["Stage 2"],
    collector_number=20,
    set_code="SM1",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Steenee.Name",
    family_id=761,
    abilities=[
        Ability(
            title="Queenly Majesty",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may have your opponent reveal their hand. Then, discard a card from it.",
            trigger=Triggers.ON_EVOLVE,
            effect=_queenly_majesty,
        ),
        Attack(
            title="Trop Kick",
            game_text="Heal 20 damage and remove all Special Conditions from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=unimplemented,
        ),
    ],
)