from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c4680470-9064-52fa-829c-b43d9f8dd798",
    key="HGSS2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vulpix.Name",
    display_name="Vulpix",
    searchable_by=["Vulpix", "Basic", "Vulpix"],
    subtypes=["Basic"],
    collector_number=68,
    set_code="HGSS2",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=37,
    abilities=[
        Attack(
            title="Fireworks",
            game_text="Flip a coin. If tails, discard a Fire Energy attached to Vulpix.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            effect=unimplemented,
        ),
    ],
)