from ptcgo.game.card_effects.attacks_common import conditions_if
from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.card_effects.trainers import card_named_contains


def defender_has(word):
    return lambda ctx: card_named_contains(word)(ctx.defender)
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4ad12660-3e7c-5b4f-b782-63a259c56b11",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasManectric.Name",
    display_name="Team Aqua's Manectric",
    searchable_by=["Team Aqua's Manectric", "Stage 1", "TeamAquasManectric"],
    subtypes=["Stage 1"],
    collector_number=29,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasElectrike.Name",
    family_id=309,
    abilities=[
        Attack(
            title="Aqua Beam",
            game_text="If the Defending Pok\u00e9mon has Team Magma in its name, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=conditions_if(defender_has("team magma"), SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Chaos Crush",
            game_text="If the Defending Pok\u00e9mon is Confused, discard an Energy card attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=unimplemented,
        ),
    ],
)