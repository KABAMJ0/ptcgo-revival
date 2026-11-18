from ptcgo.game.card_effects.attacks_common import flip_or_nothing
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0ec8a9c3-d7b7-5571-8095-e086699d7b5d",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shinx.Name",
    display_name="Shinx",
    searchable_by=["Shinx", "Basic", "Shinx"],
    subtypes=["Basic"],
    collector_number=135,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=403,
    abilities=[
        Attack(
            title="Wild Kick",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            effect=flip_or_nothing(),
        ),
    ],
)