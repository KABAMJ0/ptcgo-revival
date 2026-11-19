from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.passives_common import is_in_active_spot, prevent_damage_when
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

def _benched_grass(calc, carrier) -> bool:
    target = calc.target
    if target is None or is_in_active_spot(target):
        return False
    return PokemonTypes.GRASS.value in (target.get_attribute(AttrID.POKEMON_TYPES) or [])

card = PokemonCardDef(
    guid="8c4969f8-5ca7-5394-bb96-f3cd43fa8b3f",
    key="HGSS3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vespiquen.Name",
    display_name="Vespiquen",
    searchable_by=["Vespiquen", "Stage 1", "Vespiquen"],
    subtypes=["Stage 1"],
    collector_number=23,
    set_code="HGSS3",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Combee.Name",
    family_id=415,
    abilities=[
        Ability(
            title="Defense Sign",
            game_text="Prevent all damage done to your Benched Grass Pok\u00e9mon by attacks.",
            passive=prevent_damage_when(_benched_grass),
        ),
        Attack(
            title="Mach Wind",
            game_text="During your next turn, Vespiquen's Retreat Cost is 0.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=unimplemented,
        ),
    ],
)
