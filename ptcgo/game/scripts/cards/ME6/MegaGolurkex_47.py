from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import recoil_attack

card = PokemonCardDef(
    guid="cec017af-af36-525b-833a-785122be0bb6",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaGolurkex.Name",
    display_name="Mega Golurk ex",
    searchable_by=["Mega Golurk ex", "Stage 1", "MEGA", "ex", "MegaGolurkex"],
    subtypes=["Stage 1", "MEGA", "ex"],
    collector_number=47,
    set_code="ME6",
    rarity=Rarities.Rare,
    hp=350,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Golett.Name",
    family_id=622,
    abilities=[
        Ability(
            title="Restricted Activation",
            game_text="This Pok\u00e9mon can't use attacks unless you have 10 or more cards in your hand.",
            effect=unimplemented,
        ),
        Attack(
            title="Goliath's Punch",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=300,
            effect=recoil_attack(30),
        ),
    ],
)