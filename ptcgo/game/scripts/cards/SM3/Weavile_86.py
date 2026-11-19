from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.trainers import attacker_has_ability


async def rule_of_evil(ctx):
    """60 damage to every Pokemon that has an Ability, on both sides; the
    Bench takes it without Weakness or Resistance."""
    has_ability = attacker_has_ability()
    for pokemon in list(ctx.my_pokemon_in_play()) + list(ctx.opponent_pokemon_in_play()):
        if has_ability(pokemon):
            await ctx.deal_damage(60, target=pokemon)


card = PokemonCardDef(
    guid="2d45d205-a8f6-5227-be9b-aa2b360fe157",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Weavile.Name",
    display_name="Weavile",
    searchable_by=["Weavile", "Stage 1", "Weavile"],
    subtypes=["Stage 1"],
    collector_number=86,
    set_code="SM3",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sneasel.Name",
    family_id=215,
    abilities=[
        Attack(
            title="Rule of Evil",
            game_text="This attack does 60 damage to each Pok\u00e9mon that has an Ability (both yours and your opponent's). (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=rule_of_evil,
        ),
        Attack(
            title="Slash",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)