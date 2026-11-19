from ptcgo.game.card_effects.support_common import attach_from_hand
from ptcgo.game.card_effects.trainers import basic_energy_of
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="af17ab19-978a-5560-8dcd-f1e264fd98bf",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Groudon.Name",
    display_name="Groudon",
    searchable_by=["Groudon", "Basic", "Groudon"],
    subtypes=["Basic"],
    collector_number=93,
    set_code="SV4",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=383,
    abilities=[
        Attack(
            title="Swelling Power",
            game_text="Attach a Basic Fighting Energy card from your hand to 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=attach_from_hand(basic_energy_of("fighting"), count=1, target="choice"),
        ),
        Attack(
            title="Magma Purge",
            game_text="Discard up to 4 Energy from your Pok\u00e9mon. This attack does 60 damage for each card you discarded in this way.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)