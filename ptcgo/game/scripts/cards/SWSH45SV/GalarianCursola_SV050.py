from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import no_retreat_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from ptcgo.game.card_effects.attacks_common import condition_attack

async def perish_body(ctx):
    """If in the Active Spot and Knocked Out by damage from an opponent's
    attack, flip a coin. If heads, the Attacking Pokemon is Knocked Out."""
    if not ctx.ko_from_attack:
        return
    active_area = ctx.board.find_player_area(ctx.player_id, "activePokemonArea")
    if active_area is not None and active_area.children:
        return  # was Benched, not Active, when Knocked Out
    results = await ctx.flip_coins(1, "Perish Body")
    if results and results[0]:
        await ctx.knock_out(ctx.ko_attacker)

card = PokemonCardDef(
    guid="2fe36aa8-2c0a-5407-9f46-84006dc60a34",
    key="SWSH45SV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianCursola.Name",
    display_name="Galarian Cursola",
    searchable_by=["Galarian Cursola", "Stage 1", "GalarianCursola"],
    subtypes=["Stage 1"],
    collector_number=50,
    set_code="SWSH45SV",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianCorsola.Name",
    family_id=222,
    abilities=[
        Ability(
            title="Perish Body",
            game_text="If this Pok\u00e9mon is in the Active Spot and is Knocked Out by damage from an opponent's attack, flip a coin. If heads, the Attacking Pok\u00e9mon is Knocked Out.",
            effect=perish_body,
        ),
        Attack(
            title="Corner",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=no_retreat_attack(),
        ),
    ],
)