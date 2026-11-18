from ptcgo.game.card_effects.attacks_common import flip_or_nothing
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="042c3540-c6cc-5a6f-b054-06d0ef5380a4",
    key="HGSS1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    display_name="Slowpoke",
    searchable_by=["Slowpoke", "Basic", "Slowpoke"],
    subtypes=["Basic"],
    collector_number=81,
    set_code="HGSS1",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=79,
    abilities=[
        Attack(
            title="Whimsy Tackle",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=flip_or_nothing(),
        ),
    ],
)