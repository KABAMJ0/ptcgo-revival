from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import draw_until_effect
from ptcgo.game.data_utils import def_for


async def nine_tailed_shapeshifter(ctx):
    """Choose 1 of the opponent's Active Pokemon's attacks and use it."""
    defender = ctx.defender
    if defender is None:
        return
    definition = def_for(defender.archetype_id)
    attacks = [a for a in getattr(definition, "abilities", []) if isinstance(a, Attack)]
    if not attacks:
        return
    candidates = [(defender, atk) for atk in attacks]
    picked = await ctx.choose_attack_to_copy(candidates, "Choose an attack to copy")
    if picked is None:
        return
    _, chosen = picked
    await ctx.use_attack(chosen)


card = PokemonCardDef(
    guid="9032dc2e-723e-5216-9e2c-1e68275d02b4",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mewex.Name",
    display_name="Mew ex",
    searchable_by=["Mew ex", "Basic", "ex", "Mewex"],
    subtypes=["Basic", "ex"],
    collector_number=53,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=151,
    abilities=[
        Ability(
            title="Restart",
            game_text="Once during your turn, you may draw cards until you have 3 cards in your hand.",
            activation=Activations.ONCE_PER_TURN,
            effect=draw_until_effect(3),
        ),
        Attack(
            title="Genome Hacking",
            game_text="Choose 1 of your opponent's Active Pok\u00e9mon's attacks and use it as this attack.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=nine_tailed_shapeshifter,
        ),
    ],
)