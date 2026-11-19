from ptcgo.game.card_effects.attacks_common import flip_or_nothing
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="be88144c-032c-548e-b92f-d8ae90964d2d",
    key="HGSS3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beldum.Name",
    display_name="Beldum",
    searchable_by=["Beldum", "Basic", "Beldum"],
    subtypes=["Basic"],
    collector_number=43,
    set_code="HGSS3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=374,
    abilities=[
        Attack(
            title="Lunge Out",
            cost={PokemonTypes.METAL: 1},
            damage=10,
        ),
        Attack(
            title="Single Smash",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=flip_or_nothing(),
        ),
    ],
)