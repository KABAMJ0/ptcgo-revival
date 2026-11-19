from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.passives_common import team_damage_boost_passive
from ptcgo.game.attributes import AttrID


def _is_dragon(pokemon):
    return PokemonTypes.DRAGON.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])


_fight_song = team_damage_boost_passive(20, attacker_pred=_is_dragon)

card = PokemonCardDef(
    guid="6bc176ea-6514-5ad7-935c-303bc6b27e6d",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Altaria.Name",
    display_name="Altaria",
    searchable_by=["Altaria", "Stage 1", "Altaria"],
    subtypes=["Stage 1"],
    collector_number=40,
    set_code="DM",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Swablu.Name",
    family_id=333,
    abilities=[
        Ability(
            title="Fight Song",
            game_text="Your Dragon Pok\u00e9mon's attacks do 20 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance).",
            passive=_fight_song,
        ),
        Attack(
            title="Pierce",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)