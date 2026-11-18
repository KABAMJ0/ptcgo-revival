from ptcgo.game.card_effects.attacks_common import flip_or_nothing
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1e215bc4-cb99-5fab-9a0f-e66ecfacb6a4",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Poltchageist.Name",
    display_name="Poltchageist",
    searchable_by=["Poltchageist", "Basic", "Poltchageist"],
    subtypes=["Basic"],
    collector_number=21,
    set_code="SV6",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    abilities=[
        Attack(
            title="Tea Server",
            game_text="Put a Basic Grass Energy card from your discard pile into your hand.",
            cost={PokemonTypes.GRASS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Surprise Attack",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=flip_or_nothing(),
        ),
    ],
)