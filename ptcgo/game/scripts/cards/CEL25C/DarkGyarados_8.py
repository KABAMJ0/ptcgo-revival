from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

from ptcgo.game.card_effects.passives_common import on_ko_from_attack
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.data_utils import Triggers


async def final_beam(ctx):
    """Knocked Out by an attack: flip a coin, and on heads do 20 damage per
    Water Energy attached to Dark Gyarados to the Pokemon that Knocked it Out."""
    heads = await ctx.flip_coins(1, "Final Beam")
    if not heads or not heads[0]:
        return
    attacker = ctx.ko_attacker if ctx.ko_attacker is not None else ctx.damaged_by
    if attacker is None:
        return
    water = sum(1 for energy in ctx.attached_energies(ctx.source)
                if energy_provides_type(energy, PokemonTypes.WATER.value))
    if water <= 0:
        return
    await ctx.deal_damage(20 * water, target=attacker)


card = PokemonCardDef(
    guid="6acfde16-1598-575d-be5c-b38b05f84b8f",
    key="CEL25C",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkGyarados.Name",
    display_name="Dark Gyarados",
    searchable_by=["Dark Gyarados", "Stage 1", "DarkGyarados"],
    subtypes=["Stage 1"],
    collector_number=8,
    set_code="CEL25C",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magikarp.Name",
    family_id=130,
    abilities=[
        Ability(
            title="Final Beam",
            game_text="When Dark Gyarados is Knocked Out by an attack, flip a coin. If heads, this power does 20 damage for each Water Energy attached to Dark Gyarados to the Pok\u00e9mon that Knocked Out Dark Gyarados. Apply Weakness and Resistance. This power doesn't work if Dark Gyarados is Asleep, Confused, or Paralyzed.",
            trigger=Triggers.ON_KNOCKED_OUT,
            effect=on_ko_from_attack(final_beam),
        ),
        Attack(
            title="Ice Beam",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.WATER: 3},
            damage=30,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)