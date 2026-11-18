from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from ptcgo.game.card_effects.attacks_common import bonus_if


def _opponent_has_lightning(ctx) -> bool:
    return any(PokemonTypes.LIGHTNING.value
               in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])
               for pokemon in ctx.opponent_pokemon_in_play())

card = PokemonCardDef(
    guid="bef72908-6d50-52fd-a28b-4f5798498cec",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Heliolisk.Name",
    display_name="Heliolisk",
    searchable_by=["Heliolisk", "Stage 1", "Heliolisk"],
    subtypes=["Stage 1"],
    collector_number=180,
    set_code="SM12",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Helioptile.Name",
    family_id=694,
    abilities=[
        Attack(
            title="Parabolic Counter",
            game_text="If your opponent has any Lightning Pok\u00e9mon in play, this attack does 90 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=bonus_if(_opponent_has_lightning, 90),
        ),
        Attack(
            title="Zap Kick",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
    ],
)