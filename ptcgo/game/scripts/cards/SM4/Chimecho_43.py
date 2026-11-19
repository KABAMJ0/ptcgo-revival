from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, def_for, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


def _is_ability_pokemon(card) -> bool:
    """A Pokemon card that prints at least one Ability. PokemonCardDef.abilities
    carries Attacks too, so a truthiness test would match every Pokemon."""
    definition = def_for(getattr(card, "archetype_id", "") or "")
    if not isinstance(definition, PokemonCardDef):
        return False
    return any(not isinstance(entry, Attack)
               for entry in getattr(definition, "abilities", None) or [])


async def bell_of_silence(ctx):
    """10 damage; during your opponent's next turn they can't play a Pokemon
    that has an Ability from their hand."""
    await ctx.deal_damage()
    ctx.lock_plays(ctx.opponent_id, _is_ability_pokemon)


card = PokemonCardDef(
    guid="16316e6f-1ee2-57f1-b82b-b99869e538f0",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chimecho.Name",
    display_name="Chimecho",
    searchable_by=["Chimecho", "Basic", "Chimecho"],
    subtypes=["Basic"],
    collector_number=43,
    set_code="SM4",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=358,
    abilities=[
        Attack(
            title="Bell of Silence",
            game_text="Your opponent can't play any Pok\u00e9mon that has an Ability from their hand during their next turn.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            effect=bell_of_silence,
        ),
    ],
)