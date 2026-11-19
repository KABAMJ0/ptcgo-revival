from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

from ptcgo.game.attributes import AttrID
from ptcgo.game.card_effects.pokemon import energy_provides_type


async def core_stream(ctx):
    """Choose an Energy type other than Colorless: 20 to each opposing Pokemon
    with an Energy card of that type attached."""
    types = sorted({PokemonTypes.WATER.value, PokemonTypes.FIRE.value,
                    PokemonTypes.GRASS.value, PokemonTypes.LIGHTNING.value,
                    PokemonTypes.PSYCHIC.value, PokemonTypes.FIGHTING.value})
    from ptcgo.game.attributes import PokemonTypes as PT
    choices = [PT(value) for value in types]
    picked = await ctx.choose(
        "Choose an Energy type", [member.name.title() for member in choices])
    chosen = choices[picked if 0 <= picked < len(choices) else 0]
    for pokemon in list(ctx.opponent_pokemon_in_play()):
        if any(energy_provides_type(energy, chosen.value)
               for energy in ctx.attached_energies(pokemon)):
            await ctx.deal_damage(20, target=pokemon, apply_modifiers=False)

card = PokemonCardDef(
    guid="954e9fed-a701-5f7f-8fb9-0f4a11c814e5",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Starmie.Name",
    display_name="Starmie",
    searchable_by=["Starmie", "Stage 1", "Starmie"],
    subtypes=["Stage 1"],
    collector_number=25,
    set_code="NEO3",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Staryu.Name",
    family_id=120,
    abilities=[
        Attack(
            title="Confuse Ray",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.CONFUSED, flip=True),
        ),
        Attack(
            title="Core Stream",
            game_text="Choose an Energy type other than Colorless. This attack does 20 damage to each of your opponent's Pok\u00e9mon with any Energy cards of that type attached to it. Don't apply Weakness and Resistance.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            effect=core_stream,
        ),
    ],
)