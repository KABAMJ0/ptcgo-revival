from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import no_retreat_attack
from ptcgo.game.card_effects.passives_common import protect_next_turn

card = PokemonCardDef(
    guid="e3f1d4a3-2beb-5a7d-80ef-8db609327ab9",
    key="SWSH12PT5GG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GlaceonVSTAR.Name",
    display_name="Glaceon VSTAR",
    searchable_by=["Glaceon VSTAR", "VSTAR", "GlaceonVSTAR"],
    subtypes=["VSTAR"],
    collector_number=40,
    set_code="SWSH12PT5GG",
    rarity=Rarities.RareHoloVSTAR,
    hp=260,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.VSTAR,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GlaceonV.Name",
    family_id=471,
    abilities=[
        Attack(
            title="Icicle Shot",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
            effect=no_retreat_attack(),
        ),
        Attack(
            title="Crystal Star",
            game_text="During your opponent's next turn, prevent all damage from and effects of attacks done to this Pok\u00e9mon. (You can't use more than 1 VSTAR Power in a game.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=220,
            effect=protect_next_turn(prevent=True, effects_too=True),
        ),
    ],
)