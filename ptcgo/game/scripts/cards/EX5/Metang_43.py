from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions

card = PokemonCardDef(
    guid="679b8b11-35b7-50db-bf8c-dab9a0c0557a",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Metang.Name",
    display_name="Metang",
    searchable_by=["Metang", "Stage 1", "Metang"],
    subtypes=["Stage 1"],
    collector_number=43,
    set_code="EX5",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Beldum.Name",
    family_id=374,
    abilities=[
        Attack(
            title="Psyshock",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Metal Ball",
            game_text="Put 5 damage counters on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
    ],
)