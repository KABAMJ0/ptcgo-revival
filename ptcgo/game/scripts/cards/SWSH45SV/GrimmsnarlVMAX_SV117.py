from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import count_energy

async def g_max_drill(ctx):
    attached = count_energy("self", energy_type=PokemonTypes.DARKNESS)(ctx)
    extra = max(0, attached - 3)
    bonus = min(100, extra * 50)
    await ctx.deal_damage(170 + bonus)

card = PokemonCardDef(
    guid="6091d5ef-f4ed-5226-9559-96ead11da446",
    key="SWSH45SV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GrimmsnarlVMAX.Name",
    display_name="Grimmsnarl VMAX",
    searchable_by=["Grimmsnarl VMAX", "VMAX", "GrimmsnarlVMAX"],
    subtypes=["VMAX"],
    collector_number=117,
    set_code="SWSH45SV",
    rarity=Rarities.RareHoloVMAX,
    hp=330,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GrimmsnarlV.Name",
    family_id=861,
    abilities=[
        Attack(
            title="G-Max Drill",
            game_text="This attack does 50 more damage for each extra Darkness Energy attached to this Pok\u00e9mon (in addition to this attack's cost). You can't add more than 100 damage in this way.",
            cost={PokemonTypes.DARKNESS: 3},
            damage=170,
            damage_operator="+",
            effect=g_max_drill,
        ),
    ],
)