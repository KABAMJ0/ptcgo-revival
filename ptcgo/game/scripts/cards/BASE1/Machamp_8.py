from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.data_utils import Triggers


async def strikes_back(ctx):
    attacker = ctx.damaged_by
    if attacker is None or attacker.owning_player_id == ctx.player_id:
        return
    await ctx.deal_damage(10, target=attacker, apply_modifiers=False)

card = PokemonCardDef(
    guid="36acad07-0803-5a49-8f14-994f6eb1f47d",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Machamp.Name",
    display_name="Machamp",
    searchable_by=["Machamp", "Stage 2", "Machamp"],
    subtypes=["Stage 2"],
    collector_number=8,
    set_code="BASE1",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Machoke.Name",
    family_id=66,
    abilities=[
        Ability(
            title="Strikes Back",
            game_text="Whenever your opponent's attack damages Machamp (even if Machamp is Knocked Out), this power does 10 damage to the attacking Pok\u00e9mon. (Don't apply Weakness and Resistance.) This power can't be used if Machamp is Asleep, Confused, or Paralyzed when your opponent attacks.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=strikes_back,
        ),
        Attack(
            title="Seismic Toss",
            cost={PokemonTypes.FIGHTING: 3, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)