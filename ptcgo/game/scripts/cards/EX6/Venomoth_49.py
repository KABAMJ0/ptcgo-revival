from ptcgo.game.card_effects.attacks_common import flip_or_nothing
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_or_nothing

card = PokemonCardDef(
    guid="87a66198-7d96-54aa-934d-86ff869a5274",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Venomoth.Name",
    display_name="Venomoth",
    searchable_by=["Venomoth", "Stage 1", "Venomoth"],
    subtypes=["Stage 1"],
    collector_number=49,
    set_code="EX6",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Venonat.Name",
    family_id=48,
    abilities=[
        Ability(
            title="Protective Dust",
            game_text="Prevent all effects of attacks, except damage, done to Venomoth by the Attacking Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Sleep Poison",
            game_text="The Defending Pok\u00e9mon is now Asleep and Poisoned.",
            cost={PokemonTypes.GRASS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Razor Wind",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=flip_or_nothing(),
        ),
    ],
)