
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, def_for
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


def _is_dark_tyranitar(card) -> bool:
    return getattr(def_for(getattr(card, "archetype_id", "") or ""),
                   "display_name", "") == "Dark Tyranitar"

async def _explosive_evolution(ctx):
    """Heads: 10 to each opposing Pokemon (no W/R), then Dark Pupitar evolves
    into the Dark Tyranitar still in the deck.

    Not `evolve_from_deck(target="self")`: that helper raises NameError on its
    PokemonEntity reference (attacks_common.py:1823), so the deck search and
    the evolution are done here."""
    results = await ctx.flip_coins(1, "Explosive Evolution")
    if not (results and results[0]):
        return
    for pokemon in ctx.opponent_pokemon_in_play():
        await ctx.deal_damage(10, target=pokemon, apply_modifiers=False)
    found = await ctx.search_deck(
        _is_dark_tyranitar, count=1, minimum=0,
        prompt="Search your deck for Dark Tyranitar")
    if found and ctx.attacker is not None:
        await ctx.evolve_pokemon(ctx.attacker, found[0])
    await ctx.shuffle_deck()


async def _rock_tackle(ctx):
    """Rock Tackle: printed damage, 10 to itself and this attack locked."""
    await ctx.deal_damage()
    if ctx.attacker is not None:
        await ctx.deal_damage(10, target=ctx.attacker, apply_modifiers=False)
        ctx.session.turn_state.lock_attack(ctx.attacker.entity_id,
                                          ctx.ability.ability_id)

card = PokemonCardDef(
    guid="f335917b-8b2f-584f-b5ec-315ef27ee132",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkPupitar.Name",
    display_name="Dark Pupitar",
    searchable_by=["Dark Pupitar", "Stage 1", "DarkPupitar"],
    subtypes=["Stage 1"],
    collector_number=38,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Larvitar.Name",
    family_id=246,
    abilities=[
        Attack(
            title="Rock Tackle",
            game_text="Dark Pupitar does 10 damage to itself. Dark Pupitar can't use this attack during your next turn.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=40,
            effect=_rock_tackle,
        ),
        Attack(
            title="Explosive Evolution",
            game_text="Flip a coin. If heads, this attack does 10 damage to each of your opponent's Pok\u00e9mon. Don't apply Weakness and Resistance. Then, search your deck for an Evolution card named Dark Tyranitar and put it on Dark Pupitar. (This counts as evolving Dark Pupitar.) Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=_explosive_evolution,
        ),
    ],
)