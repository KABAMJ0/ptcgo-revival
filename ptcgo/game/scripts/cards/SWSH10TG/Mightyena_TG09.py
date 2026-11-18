from ptcgo.game.card_effects.attacks_common import recoil_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2be47b28-eb22-53b6-b109-9dc04f7abe9c",
    key="SWSH10TG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mightyena.Name",
    display_name="Mightyena",
    searchable_by=["Mightyena", "Stage 1", "Mightyena"],
    subtypes=["Stage 1"],
    collector_number=9,
    set_code="SWSH10TG",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Poochyena.Name",
    family_id=262,
    abilities=[
        Ability(
            title="Hustle Bark",
            game_text="If your opponent has any Pok\u00e9mon VMAX in play, this Pok\u00e9mon's attacks cost ColorlessColorlessColorless less.",
            effect=unimplemented,
        ),
        Attack(
            title="Wild Tackle",
            game_text="This Pok\u00e9mon also does 50 damage to itself.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=160,
            effect=recoil_attack(50),
        ),
    ],
)