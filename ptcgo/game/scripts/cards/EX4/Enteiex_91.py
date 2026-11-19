from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions

card = PokemonCardDef(
    guid="05e212e8-ad64-5ac8-a451-6768d66b2a78",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Enteiex.Name",
    display_name="Entei ex",
    searchable_by=["Entei ex", "Basic", "ex", "Enteiex"],
    subtypes=["Basic", "ex"],
    collector_number=91,
    set_code="EX4",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=244,
    abilities=[
        Attack(
            title="Searing Flame",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.BURNED, flip=True),
        ),
        Attack(
            title="Bright Flame",
            game_text="Discard 2 Energy attached to Entei ex.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=unimplemented,
        ),
    ],
)