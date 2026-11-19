from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _backup(ctx):
    """If you have fewer than 6 cards in hand, draw until you have 6."""
    shortfall = 6 - len(ctx.hand(ctx.player_id))
    if shortfall > 0:
        await ctx.draw_cards(shortfall, ctx.player_id)

card = PokemonCardDef(
    guid="3e7e0e66-6784-587c-a322-e5fd88a6fdbc",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Porygon2.Name",
    display_name="Porygon2",
    searchable_by=["Porygon2", "Stage 1", "Porygon2"],
    subtypes=["Stage 1"],
    collector_number=25,
    set_code="EX11",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Porygon.Name",
    family_id=137,
    abilities=[
        Ability(
            title="Backup",
            game_text="Once during your turn (before your attack), if you have less than 6 cards in your hand, you may draw cards until you have 6 cards in your hand. This power can't be used if Porygon2 is affected by a Special Condition.",
            effect=_backup,
        ),
        Attack(
            title="Machine Burst",
            game_text="If Porygon2 has a Technical Machine card attached to it, the Defending Pok\u00e9mon is now Asleep and Burned.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=unimplemented,
        ),
    ],
)