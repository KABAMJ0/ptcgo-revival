from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.data_utils import def_for


async def skill_thief(ctx):
    """With no cards in hand, use an attack printed on any opposing Pokemon."""
    if ctx.hand():
        return
    candidates = []
    for pokemon in ctx.opponent_pokemon_in_play():
        definition = def_for(pokemon.archetype_id)
        for attack in getattr(definition, "abilities", []) or []:
            if isinstance(attack, Attack):
                candidates.append((pokemon, attack))
    if not candidates:
        return
    picked = await ctx.choose_attack_to_copy(candidates, "Choose an attack to use")
    if picked is not None:
        await ctx.use_attack(picked[1], source=picked[0])


card = PokemonCardDef(
    guid="9478a19d-afe8-5977-bb7f-8c1f36c06f0f",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Thievul.Name",
    display_name="Thievul",
    searchable_by=["Thievul", "Stage 1", "Thievul"],
    subtypes=["Stage 1"],
    collector_number=92,
    set_code="ME5",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nickit.Name",
    family_id=827,
    abilities=[
        Attack(
            title="Skill Thief",
            game_text="If you have no cards in your hand, choose an attack from 1 of your opponent's Pok\u00e9mon in play and use it as this attack.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=skill_thief,
        ),
        Attack(
            title="Sharp Fang",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)