from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.data_utils import def_for
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

def _nidoran_f_in_play(ctx) -> bool:
    for pokemon in ctx.my_pokemon_in_play():
        definition = def_for(getattr(pokemon, "archetype_id", "") or "")
        if definition is not None and "Nidoran \u2640" in (definition.display_name or ""):
            return True
    return False


async def _pheromone_poison(ctx):
    if _nidoran_f_in_play(ctx):
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.POISONED)

card = PokemonCardDef(
    guid="7d327954-78ed-52b0-9662-30cd2d3ee494",
    key="HGSS4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nidoran.Name",
    display_name="Nidoran ♂",
    searchable_by=["Nidoran \u2642", "Basic", "Nidoran"],
    subtypes=["Basic"],
    collector_number=70,
    set_code="HGSS4",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=32,
    abilities=[
        Attack(
            title="Pheromone Poison",
            game_text="If Nidoran \u2640 is on your Bench, the Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=_pheromone_poison,
        ),
        Attack(
            title="Horn Attack",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
