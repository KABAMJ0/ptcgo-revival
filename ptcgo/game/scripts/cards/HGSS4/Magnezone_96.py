from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from ptcgo.game.card_effects.support_common import draw_until_effect

async def _lost_burn(ctx):
    pool = []
    for pokemon in ctx.my_pokemon_in_play():
        pool.extend(ctx.attached_energies(pokemon))
    if pool:
        picks = await ctx.choose_cards(
            pool, len(pool), minimum=0,
            prompt="Choose any number of Energy to put in the Lost Zone")
        if picks:
            await ctx.move_to_lost_zone(list(picks))
            await ctx.deal_damage(50 * len(picks))
            return
    await ctx.deal_damage(_printed_damage(ctx))


def _printed_damage(ctx) -> int:
    return getattr(ctx.ability, "damage", 0) or 0

card = PokemonCardDef(
    guid="1f7c3624-13ff-5839-a116-11d0b13c28af",
    key="HGSS4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magnezone.Name",
    display_name="Magnezone",
    searchable_by=["Magnezone", "Stage 2", "Prime", "Magnezone"],
    subtypes=["Stage 2", "Prime"],
    collector_number=96,
    set_code="HGSS4",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magneton.Name",
    family_id=81,
    abilities=[
        Ability(
            title="Magnetic Draw",
            game_text="Once during your turn (before your attack), you may draw cards until you have 6 cards in your hand. This power can't be used if Magnezone is affected by a Special Condition.",
            activation=Activations.ONCE_PER_TURN,
            condition=lambda board, player_id, pokemon: not pokemon.get_attribute(
                AttrID.SPECIAL_CONDITIONS),
            effect=draw_until_effect(6),
        ),
        Attack(
            title="Lost Burn",
            game_text="Put as many Energy cards attached to your Pok\u00e9mon as you like in the Lost Zone. This attack does 50 damage times the number of Energy cards put in the Lost Zone in this way.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="x",
            effect=_lost_burn,
        ),
    ],
)