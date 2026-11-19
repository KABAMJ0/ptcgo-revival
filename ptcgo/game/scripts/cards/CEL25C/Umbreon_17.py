from ptcgo.game.card_effects.attacks_common import snipe_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.attacks_common import discard_random_from_hand
from ptcgo.game.data_utils import Triggers


async def dark_ray(ctx):
    if not await ctx.ask_yes_no(
            "Choose 1 card from your opponent's hand without looking and discard it?"):
        return
    await discard_random_from_hand(ctx, player_id=ctx.opponent_id, count=1)

card = PokemonCardDef(
    guid="bc252f4c-5f24-59de-a77a-23cd3d8d95a3",
    key="CEL25C",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Umbreon.Name",
    display_name="Umbreon ★",
    searchable_by=["Umbreon \u2605", "Basic", "Star", "Umbreon"],
    subtypes=["Basic", "Star"],
    collector_number=17,
    set_code="CEL25C",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=197,
    abilities=[
        Ability(
            title="Dark Ray",
            game_text="Once during your turn, when you put Umbreon Star from your hand onto your Bench, you may choose 1 card from your opponent's hand without looking and discard it.",
            trigger=Triggers.ON_PLAY,
            effect=dark_ray,
        ),
        Attack(
            title="Feint Attack",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 30 damage to that Pok\u00e9mon. This attack's damage isn't affected by Weakness, Resistance, Pok\u00e9-Powers, Pok\u00e9-Bodies, or any other effects on that Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 2},
            effect=snipe_attack(30, pool="any", apply_modifiers=False),
        ),
    ],
)