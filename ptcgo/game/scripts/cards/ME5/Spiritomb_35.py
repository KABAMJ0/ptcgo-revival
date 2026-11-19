from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from ptcgo.game.data_utils import def_for
from ptcgo.game.session.passives import effective_max_hp


def _hide_n_sneak_in_discard(ctx) -> int:
    """Pokemon in your discard pile that print the Hide 'n' Sneak Ability."""
    return sum(
        1 for card in ctx.discard_pile()
        if any(getattr(ability, "title", "") == "Hide 'n' Sneak"
               for ability in getattr(def_for(card.archetype_id),
                                      "abilities", []) or [])
    )


async def spiritual_end(ctx):
    """With 13+ Hide 'n' Sneak Pokemon in the discard, quadruple the damage
    counters on 2 of the opponent's Pokemon."""
    if _hide_n_sneak_in_discard(ctx) < 13:
        return
    pool = [p for p in ctx.opponent_pokemon_in_play()
            if p.get_attribute(AttrID.HP, 0) < effective_max_hp(ctx.board, p)]
    if not pool:
        return
    picks = await ctx.choose_cards(pool, 2, minimum=0,
                                   prompt="Choose 2 Pokémon to quadruple")
    for pokemon in picks:
        counters = (effective_max_hp(ctx.board, pokemon)
                    - pokemon.get_attribute(AttrID.HP, 0)) // 10
        if counters > 0:
            await ctx.deal_damage(counters * 30, target=pokemon, as_counters=True,
                                  apply_modifiers=False)


card = PokemonCardDef(
    guid="5c675dd7-c3f0-5e58-8cba-e84a22acec13",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spiritomb.Name",
    display_name="Spiritomb",
    searchable_by=["Spiritomb", "Basic", "Spiritomb"],
    subtypes=["Basic"],
    collector_number=35,
    set_code="ME5",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=442,
    abilities=[
        Attack(
            title="Spiritual End",
            game_text="If you have 13 or more Pok\u00e9mon that have the Hide 'n' Sneak Ability in your discard pile, choose 2 of your opponent's Pok\u00e9mon and quadruple the number of damage counters on each of them.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=spiritual_end,
        ),
    ],
)