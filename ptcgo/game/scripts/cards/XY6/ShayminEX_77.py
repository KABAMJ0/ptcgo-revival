from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Triggers, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import draw_until_effect
from ptcgo.game.card_effects.trainers import return_pokemon_to_hand


async def sky_return(ctx):
    """30 damage, then return this Pokemon and all cards attached to it to your
    hand."""
    pokemon = ctx.attacker
    await ctx.deal_damage()
    await return_pokemon_to_hand(lambda p: p is pokemon, with_attachments="same")(ctx)


card = PokemonCardDef(
    guid="ae0d38ab-1605-535f-9c24-ffbe33d5d43a",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShayminEX.Name",
    display_name="Shaymin-EX",
    searchable_by=["Shaymin-EX", "Basic", "EX", "ShayminEX"],
    subtypes=["Basic", "EX"],
    collector_number=77,
    set_code="XY6",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=492,
    abilities=[
        Ability(
            title="Set Up",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench, you may draw cards until you have 6 cards in your hand.",
            trigger=Triggers.ON_PLAY,
            effect=draw_until_effect(6),
        ),
        Attack(
            title="Sky Return",
            game_text="Return this Pok\u00e9mon and all cards attached to it to your hand.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=sky_return,
        ),
    ],
)