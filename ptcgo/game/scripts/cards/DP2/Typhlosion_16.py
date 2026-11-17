from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f100fed8-0449-5837-9a41-0b57efecb6a9",
    key="DP2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Typhlosion.Name",
    display_name="Typhlosion",
    searchable_by=["Typhlosion", "Stage 2", "Typhlosion"],
    subtypes=["Stage 2"],
    collector_number=16,
    set_code="DP2",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Quilava.Name",
    family_id=155,
    abilities=[
        Ability(
            title="Firestarter",
            game_text="Once during your turn (before your attack), you may attach a Fire Energy card from your discard pile to 1 of your Benched Pok\u00e9mon. This power can't be used if Typhlosion is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Evaporating Heat",
            game_text="Discard a Water Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=unimplemented,
        ),
    ],
)