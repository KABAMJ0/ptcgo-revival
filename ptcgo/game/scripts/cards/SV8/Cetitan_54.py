from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import takes_less_passive

card = PokemonCardDef(
    guid="28d77eef-611a-5270-bfe2-e628c52fd93e",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cetitan.Name",
    display_name="Cetitan",
    searchable_by=["Cetitan", "Stage 1", "Cetitan"],
    subtypes=["Stage 1"],
    collector_number=54,
    set_code="SV8",
    rarity=Rarities.Common,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cetoddle.Name",
    family_id=974,
    abilities=[
        Ability(
            title="Solid Body",
            game_text="This Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            passive=takes_less_passive(30),
        ),
        Attack(
            title="Dangerous Mouth",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=150,
        ),
    ],
)