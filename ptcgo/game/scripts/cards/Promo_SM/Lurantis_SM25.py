from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import team_damage_boost_passive
from ptcgo.game.attributes import AttrID

def _grass_or_fire(pokemon):
    types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
    return PokemonTypes.GRASS.value in types or PokemonTypes.FIRE.value in types


card = PokemonCardDef(
    guid="3aec109c-047e-5da6-bf5f-01076b00bafc",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lurantis.Name",
    display_name="Lurantis",
    searchable_by=["Lurantis", "Stage 1", "Lurantis"],
    subtypes=["Stage 1"],
    collector_number=25,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Fomantis.Name",
    family_id=754,
    abilities=[
        Ability(
            title="Sunny Day",
            game_text="The attacks of your Grass Pok\u00e9mon and Fire Pok\u00e9mon do 20 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance).",
            passive=team_damage_boost_passive(20, attacker_pred=_grass_or_fire),
        ),
        Attack(
            title="Solar Beam",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
        ),
    ],
)