from ptcgo.game.card_effects.attacks_common import flip_or_nothing
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_or_nothing

card = PokemonCardDef(
    guid="46fc9ed1-3978-5cf3-951c-35fde0ec809f",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DragoniteFB.Name",
    display_name="Dragonite FB",
    searchable_by=["Dragonite FB", "Basic", "SP", "DragoniteFB"],
    subtypes=["Basic", "SP"],
    collector_number=56,
    set_code="PL3",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=149,
    abilities=[
        Attack(
            title="Mach Blow",
            game_text="If the Defending Pok\u00e9mon is a Pok\u00e9mon SP, this attack's base damage is 80 instead of 20.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Giant Tail",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=100,
            effect=flip_or_nothing(),
        ),
    ],
)